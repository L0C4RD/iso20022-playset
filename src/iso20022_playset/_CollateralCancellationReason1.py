# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralCancellationType1Choice
from . import Max35Text

class CollateralCancellationReason1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CxlRsnCd"]
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
	def CxlRsnCd(self):
		return self._CxlRsnCd

	@CxlRsnCd.setter
	def CxlRsnCd(self, value):
		self._CxlRsnCd = value if value is not None else base_types.UninitialisedField(self, 'CxlRsnCd', CollateralCancellationType1Choice, False)

	@CxlRsnCd.deleter
	def CxlRsnCd(self):
		del self._CxlRsnCd
		self._CxlRsnCd = base_types.UninitialisedField(self, 'CxlRsnCd', CollateralCancellationType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsnCd', type=CollateralCancellationType1Choice, min=1, max=1, mutex_group=None, array=False),
	))