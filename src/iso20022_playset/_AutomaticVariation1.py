# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndTrigger1
from . import Max2000Text
from . import Max35Text
from . import VariationType1Code

class AutomaticVariation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AmtAndTrggr", "_Id", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AmtAndTrggr(self):
		return self._AmtAndTrggr

	@AmtAndTrggr.setter
	def AmtAndTrggr(self, value):
		self._AmtAndTrggr = value if value is not None else base_types.UninitialisedField(self, 'AmtAndTrggr', AmountAndTrigger1, True)

	@AmtAndTrggr.deleter
	def AmtAndTrggr(self):
		del self._AmtAndTrggr
		self._AmtAndTrggr = base_types.UninitialisedField(self, 'AmtAndTrggr', AmountAndTrigger1, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', VariationType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', VariationType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtAndTrggr', type=AmountAndTrigger1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=VariationType1Code, min=1, max=1, mutex_group=None, array=False),
	))