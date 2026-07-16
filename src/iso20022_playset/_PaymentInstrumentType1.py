# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthorityRequestType1
from . import Max500Text
from . import Min8Max28NumericText

class PaymentInstrumentType1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AuthrtyReqTp", "_CardNb"]
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
		self._AuthrtyReqTp = value if value is not None else base_types.UninitialisedField(self, 'AuthrtyReqTp', AuthorityRequestType1, True)

	@AuthrtyReqTp.deleter
	def AuthrtyReqTp(self):
		del self._AuthrtyReqTp
		self._AuthrtyReqTp = base_types.UninitialisedField(self, 'AuthrtyReqTp', AuthorityRequestType1, True)

	@property
	def CardNb(self):
		return self._CardNb

	@CardNb.setter
	def CardNb(self, value):
		self._CardNb = value if value is not None else base_types.UninitialisedField(self, 'CardNb', Min8Max28NumericText, False)

	@CardNb.deleter
	def CardNb(self):
		del self._CardNb
		self._CardNb = base_types.UninitialisedField(self, 'CardNb', Min8Max28NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrtyReqTp', type=AuthorityRequestType1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardNb', type=Min8Max28NumericText, min=1, max=1, mutex_group=None, array=False),
	))