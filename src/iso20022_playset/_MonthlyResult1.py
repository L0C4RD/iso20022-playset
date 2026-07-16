# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BaseOneRate
from . import GenericIdentification165
from . import NonNegativeNumber
from . import PositiveNumber

class MonthlyResult1(base_types._BaseFieldType):

	__slots__ = ["_AvrgXcptn", "_Cvrg", "_LrgstXcptn", "_LrgstXcptnId", "_NbOfObsrvtns", "_NbOfXcptns"]
	@property
	def AvrgXcptn(self):
		return self._AvrgXcptn

	@AvrgXcptn.setter
	def AvrgXcptn(self, value):
		self._AvrgXcptn = value if value is not None else base_types.UninitialisedField(self, 'AvrgXcptn', ActiveCurrencyAndAmount, False)

	@AvrgXcptn.deleter
	def AvrgXcptn(self):
		del self._AvrgXcptn
		self._AvrgXcptn = base_types.UninitialisedField(self, 'AvrgXcptn', ActiveCurrencyAndAmount, False)

	@property
	def Cvrg(self):
		return self._Cvrg

	@Cvrg.setter
	def Cvrg(self, value):
		self._Cvrg = value if value is not None else base_types.UninitialisedField(self, 'Cvrg', BaseOneRate, False)

	@Cvrg.deleter
	def Cvrg(self):
		del self._Cvrg
		self._Cvrg = base_types.UninitialisedField(self, 'Cvrg', BaseOneRate, False)

	@property
	def LrgstXcptn(self):
		return self._LrgstXcptn

	@LrgstXcptn.setter
	def LrgstXcptn(self, value):
		self._LrgstXcptn = value if value is not None else base_types.UninitialisedField(self, 'LrgstXcptn', ActiveCurrencyAndAmount, False)

	@LrgstXcptn.deleter
	def LrgstXcptn(self):
		del self._LrgstXcptn
		self._LrgstXcptn = base_types.UninitialisedField(self, 'LrgstXcptn', ActiveCurrencyAndAmount, False)

	@property
	def LrgstXcptnId(self):
		return self._LrgstXcptnId

	@LrgstXcptnId.setter
	def LrgstXcptnId(self, value):
		self._LrgstXcptnId = value if value is not None else base_types.UninitialisedField(self, 'LrgstXcptnId', GenericIdentification165, False)

	@LrgstXcptnId.deleter
	def LrgstXcptnId(self):
		del self._LrgstXcptnId
		self._LrgstXcptnId = base_types.UninitialisedField(self, 'LrgstXcptnId', GenericIdentification165, False)

	@property
	def NbOfObsrvtns(self):
		return self._NbOfObsrvtns

	@NbOfObsrvtns.setter
	def NbOfObsrvtns(self, value):
		self._NbOfObsrvtns = value if value is not None else base_types.UninitialisedField(self, 'NbOfObsrvtns', PositiveNumber, False)

	@NbOfObsrvtns.deleter
	def NbOfObsrvtns(self):
		del self._NbOfObsrvtns
		self._NbOfObsrvtns = base_types.UninitialisedField(self, 'NbOfObsrvtns', PositiveNumber, False)

	@property
	def NbOfXcptns(self):
		return self._NbOfXcptns

	@NbOfXcptns.setter
	def NbOfXcptns(self, value):
		self._NbOfXcptns = value if value is not None else base_types.UninitialisedField(self, 'NbOfXcptns', NonNegativeNumber, False)

	@NbOfXcptns.deleter
	def NbOfXcptns(self):
		del self._NbOfXcptns
		self._NbOfXcptns = base_types.UninitialisedField(self, 'NbOfXcptns', NonNegativeNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgXcptn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cvrg', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgstXcptn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgstXcptnId', type=GenericIdentification165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfObsrvtns', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfXcptns', type=NonNegativeNumber, min=1, max=1, mutex_group=None, array=False),
	))