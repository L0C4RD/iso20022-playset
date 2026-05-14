# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Extension1 import Extension1
from ._MessageIdentification1 import MessageIdentification1
from ._References64Choice import References64Choice
from ._Status42Choice import Status42Choice

class OrderCancellationStatusReportV05(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_Ref", "_StsRpt", "_Xtnsn"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def StsRpt(self):
		return self._StsRpt

	@StsRpt.setter
	def StsRpt(self, value):
		self._StsRpt = value if type(value) != base_types.auto else self.make_default("StsRpt")

	@StsRpt.deleter
	def StsRpt(self):
		del self._StsRpt
		self._StsRpt = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References64Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRpt', type=Status42Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))