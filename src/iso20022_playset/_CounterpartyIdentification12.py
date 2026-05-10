from . import base_types
from ._PartyIdentification236Choice import PartyIdentification236Choice
from ._CountryCode import CountryCode
from ._Branch6Choice import Branch6Choice

class CounterpartyIdentification12(base_types._BaseFieldType):

	__slots__ = ["_CtryCd", "_Brnch", "_Id"]
	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if type(value) != base_types.auto else self.make_default("Brnch")

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = None

	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if type(value) != base_types.auto else self.make_default("CtryCd")

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brnch', type=Branch6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification236Choice, min=1, max=1, mutex_group=None, array=False),
	))

