# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._OriginalGroupHeader23 import OriginalGroupHeader23
from ._OriginalPaymentInstruction54 import OriginalPaymentInstruction54
from ._PaymentTransaction170 import PaymentTransaction170

class UnderlyingTransaction35(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInfAndSts", "_OrgnlPmtInfAndSts", "_TxInfAndSts"]
	@property
	def OrgnlGrpInfAndSts(self):
		return self._OrgnlGrpInfAndSts

	@OrgnlGrpInfAndSts.setter
	def OrgnlGrpInfAndSts(self, value):
		self._OrgnlGrpInfAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInfAndSts")

	@OrgnlGrpInfAndSts.deleter
	def OrgnlGrpInfAndSts(self):
		del self._OrgnlGrpInfAndSts
		self._OrgnlGrpInfAndSts = None

	@property
	def OrgnlPmtInfAndSts(self):
		return self._OrgnlPmtInfAndSts

	@OrgnlPmtInfAndSts.setter
	def OrgnlPmtInfAndSts(self, value):
		self._OrgnlPmtInfAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlPmtInfAndSts")

	@OrgnlPmtInfAndSts.deleter
	def OrgnlPmtInfAndSts(self):
		del self._OrgnlPmtInfAndSts
		self._OrgnlPmtInfAndSts = None

	@property
	def TxInfAndSts(self):
		return self._TxInfAndSts

	@TxInfAndSts.setter
	def TxInfAndSts(self, value):
		self._TxInfAndSts = value if type(value) != base_types.auto else self.make_default("TxInfAndSts")

	@TxInfAndSts.deleter
	def TxInfAndSts(self):
		del self._TxInfAndSts
		self._TxInfAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInfAndSts', type=OriginalGroupHeader23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPmtInfAndSts', type=OriginalPaymentInstruction54, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxInfAndSts', type=PaymentTransaction170, min=0, max=None, mutex_group=None, array=True),
	))