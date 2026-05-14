# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._PartyIdentification136 import PartyIdentification136
from ._SequenceRange1Choice import SequenceRange1Choice

class ResendSearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_BizDt", "_FileRef", "_OrgnlMsgNmId", "_Rcpt", "_SeqNb", "_SeqRg"]
	@property
	def BizDt(self):
		return self._BizDt

	@BizDt.setter
	def BizDt(self, value):
		self._BizDt = value if type(value) != base_types.auto else self.make_default("BizDt")

	@BizDt.deleter
	def BizDt(self):
		del self._BizDt
		self._BizDt = None

	@property
	def FileRef(self):
		return self._FileRef

	@FileRef.setter
	def FileRef(self, value):
		self._FileRef = value if type(value) != base_types.auto else self.make_default("FileRef")

	@FileRef.deleter
	def FileRef(self):
		del self._FileRef
		self._FileRef = None

	@property
	def OrgnlMsgNmId(self):
		return self._OrgnlMsgNmId

	@OrgnlMsgNmId.setter
	def OrgnlMsgNmId(self, value):
		self._OrgnlMsgNmId = value if type(value) != base_types.auto else self.make_default("OrgnlMsgNmId")

	@OrgnlMsgNmId.deleter
	def OrgnlMsgNmId(self):
		del self._OrgnlMsgNmId
		self._OrgnlMsgNmId = None

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if type(value) != base_types.auto else self.make_default("Rcpt")

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def SeqRg(self):
		return self._SeqRg

	@SeqRg.setter
	def SeqRg(self, value):
		self._SeqRg = value if type(value) != base_types.auto else self.make_default("SeqRg")

	@SeqRg.deleter
	def SeqRg(self):
		del self._SeqRg
		self._SeqRg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqRg', type=SequenceRange1Choice, min=0, max=1, mutex_group=None, array=False),
	))