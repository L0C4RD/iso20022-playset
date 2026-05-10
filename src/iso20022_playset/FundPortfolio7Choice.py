from . import base_types
import Pension5
import TaxEfficientProduct7
import GeneralInvestment2

class FundPortfolio7Choice(base_types._BaseFieldType):

	__slots__ = ["_Pnsn", "_TaxEffcntPdct", "_GnlInvstmt"]
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
	def TaxEffcntPdct(self):
		return self._TaxEffcntPdct

	@TaxEffcntPdct.setter
	def TaxEffcntPdct(self, value):
		self._TaxEffcntPdct = value if type(value) != auto else self.make_default("TaxEffcntPdct")

	@TaxEffcntPdct.deleter
	def TaxEffcntPdct(self):
		del self._TaxEffcntPdct
		self._TaxEffcntPdct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pnsn', type=Pension5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxEffcntPdct', type=TaxEfficientProduct7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GnlInvstmt', type=GeneralInvestment2, min=0, max=1, mutex_group=1, array=False),
	))

