# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitCode
from . import EntryStatus1Choice
from . import Limit2

class TransactionType2(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_FlrLmt", "_Sts"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def FlrLmt(self):
		return self._FlrLmt

	@FlrLmt.setter
	def FlrLmt(self, value):
		self._FlrLmt = value if value is not None else base_types.UninitialisedField(self, 'FlrLmt', Limit2, True)

	@FlrLmt.deleter
	def FlrLmt(self):
		del self._FlrLmt
		self._FlrLmt = base_types.UninitialisedField(self, 'FlrLmt', Limit2, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', EntryStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', EntryStatus1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlrLmt', type=Limit2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=EntryStatus1Choice, min=1, max=1, mutex_group=None, array=False),
	))