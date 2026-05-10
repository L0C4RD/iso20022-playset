import base_types
import CollateralProposalResponseType4
import CollateralProposalResponse4

class CollateralProposalResponse4Choice(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmt", "_CollPrpsl"]
	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if type(value) != auto else self.make_default("SgrtdIndpdntAmt")

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = None

	@property
	def CollPrpsl(self):
		return self._CollPrpsl

	@CollPrpsl.setter
	def CollPrpsl(self, value):
		self._CollPrpsl = value if type(value) != auto else self.make_default("CollPrpsl")

	@CollPrpsl.deleter
	def CollPrpsl(self):
		del self._CollPrpsl
		self._CollPrpsl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=CollateralProposalResponseType4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollPrpsl', type=CollateralProposalResponse4, min=0, max=1, mutex_group=1, array=False),
	))

