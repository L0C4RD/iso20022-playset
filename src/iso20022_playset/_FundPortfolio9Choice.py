# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GeneralInvestment2
from . import Pension6
from . import TaxEfficientProduct4

class FundPortfolio9Choice(base_types._BaseFieldType):

	__slots__ = ["_GnlInvstmt", "_Pnsn", "_TaxEffcntPdct"]
	@property
	def GnlInvstmt(self):
		return self._GnlInvstmt

	@GnlInvstmt.setter
	def GnlInvstmt(self, value):
		self._GnlInvstmt = value if value is not None else base_types.UninitialisedField(self, 'GnlInvstmt', GeneralInvestment2, False)

	@GnlInvstmt.deleter
	def GnlInvstmt(self):
		del self._GnlInvstmt
		self._GnlInvstmt = base_types.UninitialisedField(self, 'GnlInvstmt', GeneralInvestment2, False)

	@property
	def Pnsn(self):
		return self._Pnsn

	@Pnsn.setter
	def Pnsn(self, value):
		self._Pnsn = value if value is not None else base_types.UninitialisedField(self, 'Pnsn', Pension6, False)

	@Pnsn.deleter
	def Pnsn(self):
		del self._Pnsn
		self._Pnsn = base_types.UninitialisedField(self, 'Pnsn', Pension6, False)

	@property
	def TaxEffcntPdct(self):
		return self._TaxEffcntPdct

	@TaxEffcntPdct.setter
	def TaxEffcntPdct(self, value):
		self._TaxEffcntPdct = value if value is not None else base_types.UninitialisedField(self, 'TaxEffcntPdct', TaxEfficientProduct4, False)

	@TaxEffcntPdct.deleter
	def TaxEffcntPdct(self):
		del self._TaxEffcntPdct
		self._TaxEffcntPdct = base_types.UninitialisedField(self, 'TaxEffcntPdct', TaxEfficientProduct4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GnlInvstmt', type=GeneralInvestment2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pnsn', type=Pension6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxEffcntPdct', type=TaxEfficientProduct4, min=0, max=1, mutex_group=1, array=False),
	))