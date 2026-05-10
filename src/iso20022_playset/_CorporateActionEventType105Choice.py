from . import base_types
from ._CorporateActionEventType35Code import CorporateActionEventType35Code
from ._ExtendedEventType7Code import ExtendedEventType7Code

class CorporateActionEventType105Choice(base_types._BaseFieldType):

	__slots__ = ["_XtndedCorpEvtTp", "_PlainCorpEvtTp"]
	@property
	def PlainCorpEvtTp(self):
		return self._PlainCorpEvtTp

	@PlainCorpEvtTp.setter
	def PlainCorpEvtTp(self, value):
		self._PlainCorpEvtTp = value if type(value) != base_types.auto else self.make_default("PlainCorpEvtTp")

	@PlainCorpEvtTp.deleter
	def PlainCorpEvtTp(self):
		del self._PlainCorpEvtTp
		self._PlainCorpEvtTp = None

	@property
	def XtndedCorpEvtTp(self):
		return self._XtndedCorpEvtTp

	@XtndedCorpEvtTp.setter
	def XtndedCorpEvtTp(self, value):
		self._XtndedCorpEvtTp = value if type(value) != base_types.auto else self.make_default("XtndedCorpEvtTp")

	@XtndedCorpEvtTp.deleter
	def XtndedCorpEvtTp(self):
		del self._XtndedCorpEvtTp
		self._XtndedCorpEvtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlainCorpEvtTp', type=CorporateActionEventType35Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedCorpEvtTp', type=ExtendedEventType7Code, min=0, max=1, mutex_group=1, array=False),
	))

