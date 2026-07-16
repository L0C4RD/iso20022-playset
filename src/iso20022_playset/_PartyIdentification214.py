# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import PartyAddress1
from . import PartyIdentification203Choice

class PartyIdentification214(base_types._BaseFieldType):

	__slots__ = ["_Id", "_RcptNm", "_RspnRcptAdr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification203Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification203Choice, False)

	@property
	def RcptNm(self):
		return self._RcptNm

	@RcptNm.setter
	def RcptNm(self, value):
		self._RcptNm = value if value is not None else base_types.UninitialisedField(self, 'RcptNm', Max350Text, False)

	@RcptNm.deleter
	def RcptNm(self):
		del self._RcptNm
		self._RcptNm = base_types.UninitialisedField(self, 'RcptNm', Max350Text, False)

	@property
	def RspnRcptAdr(self):
		return self._RspnRcptAdr

	@RspnRcptAdr.setter
	def RspnRcptAdr(self, value):
		self._RspnRcptAdr = value if value is not None else base_types.UninitialisedField(self, 'RspnRcptAdr', PartyAddress1, False)

	@RspnRcptAdr.deleter
	def RspnRcptAdr(self):
		del self._RspnRcptAdr
		self._RspnRcptAdr = base_types.UninitialisedField(self, 'RspnRcptAdr', PartyAddress1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification203Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRcptAdr', type=PartyAddress1, min=1, max=1, mutex_group=None, array=False),
	))