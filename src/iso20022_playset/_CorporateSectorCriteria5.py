from . import base_types
from ._NotReported1Code import NotReported1Code
from ._NACEDomainIdentifier import NACEDomainIdentifier
from ._FinancialPartySectorType2Code import FinancialPartySectorType2Code

class CorporateSectorCriteria5(base_types._BaseFieldType):

	__slots__ = ["_NotRptd", "_NFISctr", "_FISctr"]
	@property
	def FISctr(self):
		return self._FISctr

	@FISctr.setter
	def FISctr(self, value):
		self._FISctr = value if type(value) != base_types.auto else self.make_default("FISctr")

	@FISctr.deleter
	def FISctr(self):
		del self._FISctr
		self._FISctr = None

	@property
	def NFISctr(self):
		return self._NFISctr

	@NFISctr.setter
	def NFISctr(self, value):
		self._NFISctr = value if type(value) != base_types.auto else self.make_default("NFISctr")

	@NFISctr.deleter
	def NFISctr(self):
		del self._NFISctr
		self._NFISctr = None

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if type(value) != base_types.auto else self.make_default("NotRptd")

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FISctr', type=FinancialPartySectorType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NFISctr', type=NACEDomainIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=None, array=False),
	))

