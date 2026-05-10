import base_types
import CreditDebitCode
import Limit2
import EntryStatus1Choice

class TransactionType2(base_types._BaseFieldType):

	__slots__ = ["_FlrLmt", "_CdtDbtInd", "_Sts"]
	@property
	def FlrLmt(self):
		return self._FlrLmt

	@FlrLmt.setter
	def FlrLmt(self, value):
		self._FlrLmt = value if type(value) != auto else self.make_default("FlrLmt")

	@FlrLmt.deleter
	def FlrLmt(self):
		del self._FlrLmt
		self._FlrLmt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FlrLmt', type=Limit2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=EntryStatus1Choice, min=1, max=1, mutex_group=None, array=False),
	))

