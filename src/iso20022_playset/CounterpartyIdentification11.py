import base_types
import Branch5Choice
import CollateralRole1Code
import OrganisationIdentification15Choice
import CounterpartyTradeNature7Choice

class CounterpartyIdentification11(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Sd", "_Brnch", "_Ntr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if type(value) != auto else self.make_default("Sd")

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = None

	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if type(value) != auto else self.make_default("Brnch")

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = None

	@property
	def Ntr(self):
		return self._Ntr

	@Ntr.setter
	def Ntr(self, value):
		self._Ntr = value if type(value) != auto else self.make_default("Ntr")

	@Ntr.deleter
	def Ntr(self):
		del self._Ntr
		self._Ntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sd', type=CollateralRole1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnch', type=Branch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntr', type=CounterpartyTradeNature7Choice, min=0, max=1, mutex_group=None, array=False),
	))

