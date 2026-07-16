# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OriginalGroupHeader21
from . import PaymentTransaction155

class UnderlyingTransaction34(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInfAndCxl", "_TxInf"]
	@property
	def OrgnlGrpInfAndCxl(self):
		return self._OrgnlGrpInfAndCxl

	@OrgnlGrpInfAndCxl.setter
	def OrgnlGrpInfAndCxl(self, value):
		self._OrgnlGrpInfAndCxl = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInfAndCxl', OriginalGroupHeader21, False)

	@OrgnlGrpInfAndCxl.deleter
	def OrgnlGrpInfAndCxl(self):
		del self._OrgnlGrpInfAndCxl
		self._OrgnlGrpInfAndCxl = base_types.UninitialisedField(self, 'OrgnlGrpInfAndCxl', OriginalGroupHeader21, False)

	@property
	def TxInf(self):
		return self._TxInf

	@TxInf.setter
	def TxInf(self, value):
		self._TxInf = value if value is not None else base_types.UninitialisedField(self, 'TxInf', PaymentTransaction155, True)

	@TxInf.deleter
	def TxInf(self):
		del self._TxInf
		self._TxInf = base_types.UninitialisedField(self, 'TxInf', PaymentTransaction155, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInfAndCxl', type=OriginalGroupHeader21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxInf', type=PaymentTransaction155, min=0, max=None, mutex_group=None, array=True),
	))