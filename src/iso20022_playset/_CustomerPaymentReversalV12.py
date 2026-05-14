# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GroupHeader124 import GroupHeader124
from ._OriginalGroupHeader20 import OriginalGroupHeader20
from ._OriginalPaymentInstruction50 import OriginalPaymentInstruction50
from ._SupplementaryData1 import SupplementaryData1

class CustomerPaymentReversalV12(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_OrgnlGrpInf", "_OrgnlPmtInfAndRvsl", "_SplmtryData"]
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
	def OrgnlPmtInfAndRvsl(self):
		return self._OrgnlPmtInfAndRvsl

	@OrgnlPmtInfAndRvsl.setter
	def OrgnlPmtInfAndRvsl(self, value):
		self._OrgnlPmtInfAndRvsl = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfAndRvsl")

	@OrgnlPmtInfAndRvsl.deleter
	def OrgnlPmtInfAndRvsl(self):
		del self._OrgnlPmtInfAndRvsl
		self._OrgnlPmtInfAndRvsl = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader124, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupHeader20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfAndRvsl', type=OriginalPaymentInstruction50, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))