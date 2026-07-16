# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorityRequestType1
from . import DateOrDateTimePeriod1Choice
from . import InvestigationResult1Choice
from . import Max500Text

class ReturnIndicator2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AuthrtyReqTp", "_InvstgtnRslt", "_RspnPrd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max500Text, False)

	@property
	def AuthrtyReqTp(self):
		return self._AuthrtyReqTp

	@AuthrtyReqTp.setter
	def AuthrtyReqTp(self, value):
		self._AuthrtyReqTp = value if value is not None else base_types.UninitialisedField(self, 'AuthrtyReqTp', AuthorityRequestType1, False)

	@AuthrtyReqTp.deleter
	def AuthrtyReqTp(self):
		del self._AuthrtyReqTp
		self._AuthrtyReqTp = base_types.UninitialisedField(self, 'AuthrtyReqTp', AuthorityRequestType1, False)

	@property
	def InvstgtnRslt(self):
		return self._InvstgtnRslt

	@InvstgtnRslt.setter
	def InvstgtnRslt(self, value):
		self._InvstgtnRslt = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnRslt', InvestigationResult1Choice, False)

	@InvstgtnRslt.deleter
	def InvstgtnRslt(self):
		del self._InvstgtnRslt
		self._InvstgtnRslt = base_types.UninitialisedField(self, 'InvstgtnRslt', InvestigationResult1Choice, False)

	@property
	def RspnPrd(self):
		return self._RspnPrd

	@RspnPrd.setter
	def RspnPrd(self, value):
		self._RspnPrd = value if value is not None else base_types.UninitialisedField(self, 'RspnPrd', DateOrDateTimePeriod1Choice, False)

	@RspnPrd.deleter
	def RspnPrd(self):
		del self._RspnPrd
		self._RspnPrd = base_types.UninitialisedField(self, 'RspnPrd', DateOrDateTimePeriod1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrtyReqTp', type=AuthorityRequestType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnRslt', type=InvestigationResult1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnPrd', type=DateOrDateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))