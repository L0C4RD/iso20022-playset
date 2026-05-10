from . import base_types
from ._Max35Text import Max35Text
from ._ActionType8Code import ActionType8Code
from ._Max256Text import Max256Text

class RecommendationAction1(base_types._BaseFieldType):

	__slots__ = ["_OthrActn", "_Actn", "_Dtls"]
	@property
	def OthrActn(self):
		return self._OthrActn

	@OthrActn.setter
	def OthrActn(self, value):
		self._OthrActn = value if type(value) != base_types.auto else self.make_default("OthrActn")

	@OthrActn.deleter
	def OthrActn(self):
		del self._OthrActn
		self._OthrActn = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != base_types.auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def Dtls(self):
		return self._Dtls

	@Dtls.setter
	def Dtls(self, value):
		self._Dtls = value if type(value) != base_types.auto else self.make_default("Dtls")

	@Dtls.deleter
	def Dtls(self):
		del self._Dtls
		self._Dtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrActn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=ActionType8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dtls', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
	))

