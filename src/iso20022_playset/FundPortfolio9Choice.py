import base_types
import GeneralInvestment2
import TaxEfficientProduct4
import Pension6

class FundPortfolio9Choice(base_types._BaseFieldType):

	__slots__ = ["_Pnsn", "_GnlInvstmt", "_TaxEffcntPdct"]
	@property
	def Pnsn(self):
		return self._Pnsn

	@Pnsn.setter
	def Pnsn(self, value):
		self._Pnsn = value if type(value) != auto else self.make_default("Pnsn")

	@Pnsn.deleter
	def Pnsn(self):
		del self._Pnsn
		self._Pnsn = None

	@property
	def GnlInvstmt(self):
		return self._GnlInvstmt

	@GnlInvstmt.setter
	def GnlInvstmt(self, value):
		self._GnlInvstmt = value if type(value) != auto else self.make_default("GnlInvstmt")

	@GnlInvstmt.deleter
	def GnlInvstmt(self):
		del self._GnlInvstmt
		self._GnlInvstmt = None

	@property
	def TaxEffcntPdct(self):
		return self._TaxEffcntPdct

	@TaxEffcntPdct.setter
	def TaxEffcntPdct(self, value):
		self._TaxEffcntPdct = value if type(value) != auto else self.make_default("TaxEffcntPdct")

	@TaxEffcntPdct.deleter
	def TaxEffcntPdct(self):
		del self._TaxEffcntPdct
		self._TaxEffcntPdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pnsn', type=Pension6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GnlInvstmt', type=GeneralInvestment2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxEffcntPdct', type=TaxEfficientProduct4, min=0, max=1, mutex_group=1, array=False),
	))

