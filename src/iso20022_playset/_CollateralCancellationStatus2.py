# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import RejectionStatus3
from . import Status4Code

class CollateralCancellationStatus2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CollStsCd", "_RjctnDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max35Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max35Text, False)

	@property
	def CollStsCd(self):
		return self._CollStsCd

	@CollStsCd.setter
	def CollStsCd(self, value):
		self._CollStsCd = value if value is not None else base_types.UninitialisedField(self, 'CollStsCd', Status4Code, False)

	@CollStsCd.deleter
	def CollStsCd(self):
		del self._CollStsCd
		self._CollStsCd = base_types.UninitialisedField(self, 'CollStsCd', Status4Code, False)

	@property
	def RjctnDtls(self):
		return self._RjctnDtls

	@RjctnDtls.setter
	def RjctnDtls(self, value):
		self._RjctnDtls = value if value is not None else base_types.UninitialisedField(self, 'RjctnDtls', RejectionStatus3, False)

	@RjctnDtls.deleter
	def RjctnDtls(self):
		del self._RjctnDtls
		self._RjctnDtls = base_types.UninitialisedField(self, 'RjctnDtls', RejectionStatus3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollStsCd', type=Status4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnDtls', type=RejectionStatus3, min=0, max=1, mutex_group=None, array=False),
	))