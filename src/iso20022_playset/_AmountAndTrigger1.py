# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrPercentage1Choice
from . import Max35Text
from . import Trigger1

class AmountAndTrigger1(base_types._BaseFieldType):

	__slots__ = ["_AmtDtlsChc", "_Id", "_Trggr"]
	@property
	def AmtDtlsChc(self):
		return self._AmtDtlsChc

	@AmtDtlsChc.setter
	def AmtDtlsChc(self, value):
		self._AmtDtlsChc = value if value is not None else base_types.UninitialisedField(self, 'AmtDtlsChc', AmountOrPercentage1Choice, False)

	@AmtDtlsChc.deleter
	def AmtDtlsChc(self):
		del self._AmtDtlsChc
		self._AmtDtlsChc = base_types.UninitialisedField(self, 'AmtDtlsChc', AmountOrPercentage1Choice, False)

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
	def Trggr(self):
		return self._Trggr

	@Trggr.setter
	def Trggr(self, value):
		self._Trggr = value if value is not None else base_types.UninitialisedField(self, 'Trggr', Trigger1, True)

	@Trggr.deleter
	def Trggr(self):
		del self._Trggr
		self._Trggr = base_types.UninitialisedField(self, 'Trggr', Trigger1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtDtlsChc', type=AmountOrPercentage1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trggr', type=Trigger1, min=1, max=None, mutex_group=None, array=True),
	))