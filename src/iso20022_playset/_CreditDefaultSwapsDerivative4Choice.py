# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDefaultSwapDerivative5
from . import CreditDefaultSwapDerivative6
from . import CreditDefaultSwapIndex3
from . import CreditDefaultSwapSingleName2

class CreditDefaultSwapsDerivative4Choice(base_types._BaseFieldType):

	__slots__ = ["_CdtDfltSwpIndx", "_CdtDfltSwpIndxDeriv", "_SnglNmCdtDfltSwp", "_SnglNmCdtDfltSwpDeriv"]
	@property
	def CdtDfltSwpIndx(self):
		return self._CdtDfltSwpIndx

	@CdtDfltSwpIndx.setter
	def CdtDfltSwpIndx(self, value):
		self._CdtDfltSwpIndx = value if value is not None else base_types.UninitialisedField(self, 'CdtDfltSwpIndx', CreditDefaultSwapIndex3, False)

	@CdtDfltSwpIndx.deleter
	def CdtDfltSwpIndx(self):
		del self._CdtDfltSwpIndx
		self._CdtDfltSwpIndx = base_types.UninitialisedField(self, 'CdtDfltSwpIndx', CreditDefaultSwapIndex3, False)

	@property
	def CdtDfltSwpIndxDeriv(self):
		return self._CdtDfltSwpIndxDeriv

	@CdtDfltSwpIndxDeriv.setter
	def CdtDfltSwpIndxDeriv(self, value):
		self._CdtDfltSwpIndxDeriv = value if value is not None else base_types.UninitialisedField(self, 'CdtDfltSwpIndxDeriv', CreditDefaultSwapDerivative5, False)

	@CdtDfltSwpIndxDeriv.deleter
	def CdtDfltSwpIndxDeriv(self):
		del self._CdtDfltSwpIndxDeriv
		self._CdtDfltSwpIndxDeriv = base_types.UninitialisedField(self, 'CdtDfltSwpIndxDeriv', CreditDefaultSwapDerivative5, False)

	@property
	def SnglNmCdtDfltSwp(self):
		return self._SnglNmCdtDfltSwp

	@SnglNmCdtDfltSwp.setter
	def SnglNmCdtDfltSwp(self, value):
		self._SnglNmCdtDfltSwp = value if value is not None else base_types.UninitialisedField(self, 'SnglNmCdtDfltSwp', CreditDefaultSwapSingleName2, False)

	@SnglNmCdtDfltSwp.deleter
	def SnglNmCdtDfltSwp(self):
		del self._SnglNmCdtDfltSwp
		self._SnglNmCdtDfltSwp = base_types.UninitialisedField(self, 'SnglNmCdtDfltSwp', CreditDefaultSwapSingleName2, False)

	@property
	def SnglNmCdtDfltSwpDeriv(self):
		return self._SnglNmCdtDfltSwpDeriv

	@SnglNmCdtDfltSwpDeriv.setter
	def SnglNmCdtDfltSwpDeriv(self, value):
		self._SnglNmCdtDfltSwpDeriv = value if value is not None else base_types.UninitialisedField(self, 'SnglNmCdtDfltSwpDeriv', CreditDefaultSwapDerivative6, False)

	@SnglNmCdtDfltSwpDeriv.deleter
	def SnglNmCdtDfltSwpDeriv(self):
		del self._SnglNmCdtDfltSwpDeriv
		self._SnglNmCdtDfltSwpDeriv = base_types.UninitialisedField(self, 'SnglNmCdtDfltSwpDeriv', CreditDefaultSwapDerivative6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDfltSwpIndx', type=CreditDefaultSwapIndex3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CdtDfltSwpIndxDeriv', type=CreditDefaultSwapDerivative5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SnglNmCdtDfltSwp', type=CreditDefaultSwapSingleName2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SnglNmCdtDfltSwpDeriv', type=CreditDefaultSwapDerivative6, min=0, max=1, mutex_group=1, array=False),
	))