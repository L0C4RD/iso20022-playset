# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GroupHeader127 import GroupHeader127
from ._OriginalGroupHeader20 import OriginalGroupHeader20
from ._PaymentTransaction149 import PaymentTransaction149
from ._SupplementaryData1 import SupplementaryData1

class FIToFIPaymentReversalV13(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_OrgnlGrpInf", "_SplmtryData", "_TxInf"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if type(value) != base_types.auto else self.make_default("TxInf")

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader127, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupHeader20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInf', type=PaymentTransaction149, min=0, max=None, mutex_group=None, array=True),
	))