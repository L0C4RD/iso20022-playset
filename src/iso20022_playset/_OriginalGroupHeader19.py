# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text
from . import PaymentReturnReason7

class OriginalGroupHeader19(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCreDtTm", "_OrgnlMsgId", "_OrgnlMsgNmId", "_RtrRsnInf"]
	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@property
	def OrgnlMsgId(self):
		return self._OrgnlMsgId

	@OrgnlMsgId.setter
	def OrgnlMsgId(self, value):
		self._OrgnlMsgId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@OrgnlMsgId.deleter
	def OrgnlMsgId(self):
		del self._OrgnlMsgId
		self._OrgnlMsgId = base_types.UninitialisedField(self, 'OrgnlMsgId', Max35Text, False)

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgNmId', Max35Text, False)

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = base_types.UninitialisedField(self, 'OrgnlMsgNmId', Max35Text, False)

	@property
	def RtrRsnInf(self):
		return self._RtrRsnInf

	@RtrRsnInf.setter
	def RtrRsnInf(self, value):
		self._RtrRsnInf = value if value is not None else base_types.UninitialisedField(self, 'RtrRsnInf', PaymentReturnReason7, True)

	@RtrRsnInf.deleter
	def RtrRsnInf(self):
		del self._RtrRsnInf
		self._RtrRsnInf = base_types.UninitialisedField(self, 'RtrRsnInf', PaymentReturnReason7, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrRsnInf', type=PaymentReturnReason7, min=0, max=None, mutex_group=None, array=True),
	))