from . import base_types
from .CorporateActionEventReference3Choice import CorporateActionEventReference3Choice
from .ProcessingPosition7Choice import ProcessingPosition7Choice

class CorporateActionEventReference3(base_types._BaseFieldType):

	__slots__ = ["_LkgTp", "_EvtId"]
	@property
	def LkgTp(self):
		return self._LkgTp

	@LkgTp.setter
	def LkgTp(self, value):
		self._LkgTp = value if type(value) != base_types.auto else self.make_default("LkgTp")

	@LkgTp.deleter
	def LkgTp(self):
		del self._LkgTp
		self._LkgTp = None

	@property
	def EvtId(self):
		return self._EvtId

	@EvtId.setter
	def EvtId(self, value):
		self._EvtId = value if type(value) != base_types.auto else self.make_default("EvtId")

	@EvtId.deleter
	def EvtId(self):
		del self._EvtId
		self._EvtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtId', type=CorporateActionEventReference3Choice, min=1, max=1, mutex_group=None, array=False),
	))

