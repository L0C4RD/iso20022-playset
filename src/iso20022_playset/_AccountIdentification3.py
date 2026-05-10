from . import base_types
from ._AccountIdentification1 import AccountIdentification1
from ._Exact4AlphaNumericText import Exact4AlphaNumericText
from ._Max8Text import Max8Text

class AccountIdentification3(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Inf", "_Issr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if type(value) != base_types.auto else self.make_default("Inf")

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AccountIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Inf', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max8Text, min=1, max=1, mutex_group=None, array=False),
	))

