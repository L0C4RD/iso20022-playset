# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BaseOneRate import BaseOneRate
from ._GenericIdentification165 import GenericIdentification165
from ._NonNegativeNumber import NonNegativeNumber
from ._PositiveNumber import PositiveNumber

class MonthlyResult1(base_types._BaseFieldType):

	__slots__ = ["_AvrgXcptn", "_Cvrg", "_LrgstXcptn", "_LrgstXcptnId", "_NbOfObsrvtns", "_NbOfXcptns"]
	@property
	def AvrgXcptn(self):
		return self._AvrgXcptn

	@AvrgXcptn.setter
	def AvrgXcptn(self, value):
		self._AvrgXcptn = value if type(value) != base_types.auto else self.make_default("AvrgXcptn")

	@AvrgXcptn.deleter
	def AvrgXcptn(self):
		del self._AvrgXcptn
		self._AvrgXcptn = None

	@property
	def Cvrg(self):
		return self._Cvrg

	@Cvrg.setter
	def Cvrg(self, value):
		self._Cvrg = value if type(value) != base_types.auto else self.make_default("Cvrg")

	@Cvrg.deleter
	def Cvrg(self):
		del self._Cvrg
		self._Cvrg = None

	@property
	def LrgstXcptn(self):
		return self._LrgstXcptn

	@LrgstXcptn.setter
	def LrgstXcptn(self, value):
		self._LrgstXcptn = value if type(value) != base_types.auto else self.make_default("LrgstXcptn")

	@LrgstXcptn.deleter
	def LrgstXcptn(self):
		del self._LrgstXcptn
		self._LrgstXcptn = None

	@property
	def LrgstXcptnId(self):
		return self._LrgstXcptnId

	@LrgstXcptnId.setter
	def LrgstXcptnId(self, value):
		self._LrgstXcptnId = value if type(value) != base_types.auto else self.make_default("LrgstXcptnId")

	@LrgstXcptnId.deleter
	def LrgstXcptnId(self):
		del self._LrgstXcptnId
		self._LrgstXcptnId = None

	@property
	def NbOfObsrvtns(self):
		return self._NbOfObsrvtns

	@NbOfObsrvtns.setter
	def NbOfObsrvtns(self, value):
		self._NbOfObsrvtns = value if type(value) != base_types.auto else self.make_default("NbOfObsrvtns")

	@NbOfObsrvtns.deleter
	def NbOfObsrvtns(self):
		del self._NbOfObsrvtns
		self._NbOfObsrvtns = None

	@property
	def NbOfXcptns(self):
		return self._NbOfXcptns

	@NbOfXcptns.setter
	def NbOfXcptns(self, value):
		self._NbOfXcptns = value if type(value) != base_types.auto else self.make_default("NbOfXcptns")

	@NbOfXcptns.deleter
	def NbOfXcptns(self):
		del self._NbOfXcptns
		self._NbOfXcptns = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgXcptn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cvrg', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgstXcptn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LrgstXcptnId', type=GenericIdentification165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfObsrvtns', type=PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfXcptns', type=NonNegativeNumber, min=1, max=1, mutex_group=None, array=False),
	))