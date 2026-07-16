# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import CollateralAmount9

class ValuationsDetails2(base_types._BaseFieldType):

	__slots__ = ["_Hrcut", "_ValtnDtlsAmt"]
	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', BaseOneRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', BaseOneRate, False)

	@property
	def ValtnDtlsAmt(self):
		return self._ValtnDtlsAmt

	@ValtnDtlsAmt.setter
	def ValtnDtlsAmt(self, value):
		self._ValtnDtlsAmt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDtlsAmt', CollateralAmount9, True)

	@ValtnDtlsAmt.deleter
	def ValtnDtlsAmt(self):
		del self._ValtnDtlsAmt
		self._ValtnDtlsAmt = base_types.UninitialisedField(self, 'ValtnDtlsAmt', CollateralAmount9, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrcut', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtlsAmt', type=CollateralAmount9, min=1, max=None, mutex_group=None, array=True),
	))