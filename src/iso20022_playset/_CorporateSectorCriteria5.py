# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialPartySectorType2Code
from . import NACEDomainIdentifier
from . import NotReported1Code

class CorporateSectorCriteria5(base_types._BaseFieldType):

	__slots__ = ["_FISctr", "_NFISctr", "_NotRptd"]
	@property
	def FISctr(self):
		return self._FISctr

	@FISctr.setter
	def FISctr(self, value):
		self._FISctr = value if value is not None else base_types.UninitialisedField(self, 'FISctr', FinancialPartySectorType2Code, True)

	@FISctr.deleter
	def FISctr(self):
		del self._FISctr
		self._FISctr = base_types.UninitialisedField(self, 'FISctr', FinancialPartySectorType2Code, True)

	@property
	def NFISctr(self):
		return self._NFISctr

	@NFISctr.setter
	def NFISctr(self, value):
		self._NFISctr = value if value is not None else base_types.UninitialisedField(self, 'NFISctr', NACEDomainIdentifier, True)

	@NFISctr.deleter
	def NFISctr(self):
		del self._NFISctr
		self._NFISctr = base_types.UninitialisedField(self, 'NFISctr', NACEDomainIdentifier, True)

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if value is not None else base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FISctr', type=FinancialPartySectorType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NFISctr', type=NACEDomainIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=None, array=False),
	))