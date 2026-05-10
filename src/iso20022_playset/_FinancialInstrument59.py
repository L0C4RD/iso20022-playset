from . import base_types
from .ISINOct2015Identifier import ISINOct2015Identifier
from .SNA2008SectorIdentifier import SNA2008SectorIdentifier
from .LEIIdentifier import LEIIdentifier

class FinancialInstrument59(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_Sctr", "_Id"]
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

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != base_types.auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

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
		base_types.FieldEntry(name='Issr', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=SNA2008SectorIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

