# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat49Choice
from . import DateFormat54Choice

class CorporateActionEventDeadlines4(base_types._BaseFieldType):

	__slots__ = ["_CoverPrtctDdln", "_EarlyRspnDdln", "_MktDdln", "_PrtctDdln", "_RspnDdln"]
	@property
	def CoverPrtctDdln(self):
		return self._CoverPrtctDdln

	@CoverPrtctDdln.setter
	def CoverPrtctDdln(self, value):
		self._CoverPrtctDdln = value if value is not None else base_types.UninitialisedField(self, 'CoverPrtctDdln', DateFormat49Choice, False)

	@CoverPrtctDdln.deleter
	def CoverPrtctDdln(self):
		del self._CoverPrtctDdln
		self._CoverPrtctDdln = base_types.UninitialisedField(self, 'CoverPrtctDdln', DateFormat49Choice, False)

	@property
	def EarlyRspnDdln(self):
		return self._EarlyRspnDdln

	@EarlyRspnDdln.setter
	def EarlyRspnDdln(self, value):
		self._EarlyRspnDdln = value if value is not None else base_types.UninitialisedField(self, 'EarlyRspnDdln', DateFormat49Choice, False)

	@EarlyRspnDdln.deleter
	def EarlyRspnDdln(self):
		del self._EarlyRspnDdln
		self._EarlyRspnDdln = base_types.UninitialisedField(self, 'EarlyRspnDdln', DateFormat49Choice, False)

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if value is not None else base_types.UninitialisedField(self, 'MktDdln', DateFormat49Choice, False)

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = base_types.UninitialisedField(self, 'MktDdln', DateFormat49Choice, False)

	@property
	def PrtctDdln(self):
		return self._PrtctDdln

	@PrtctDdln.setter
	def PrtctDdln(self, value):
		self._PrtctDdln = value if value is not None else base_types.UninitialisedField(self, 'PrtctDdln', DateFormat49Choice, False)

	@PrtctDdln.deleter
	def PrtctDdln(self):
		del self._PrtctDdln
		self._PrtctDdln = base_types.UninitialisedField(self, 'PrtctDdln', DateFormat49Choice, False)

	@property
	def RspnDdln(self):
		return self._RspnDdln

	@RspnDdln.setter
	def RspnDdln(self, value):
		self._RspnDdln = value if value is not None else base_types.UninitialisedField(self, 'RspnDdln', DateFormat54Choice, False)

	@RspnDdln.deleter
	def RspnDdln(self):
		del self._RspnDdln
		self._RspnDdln = base_types.UninitialisedField(self, 'RspnDdln', DateFormat54Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CoverPrtctDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyRspnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdln', type=DateFormat54Choice, min=0, max=1, mutex_group=None, array=False),
	))