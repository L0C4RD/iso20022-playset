# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat46Choice
from . import Max35Text
from . import SecurityIdentification19

class DisclosureRequestIdentification1(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_IssrDsclsrReqId", "_ShrhldrsDsclsrRcrdDt"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def IssrDsclsrReqId(self):
		return self._IssrDsclsrReqId

	@IssrDsclsrReqId.setter
	def IssrDsclsrReqId(self, value):
		self._IssrDsclsrReqId = value if value is not None else base_types.UninitialisedField(self, 'IssrDsclsrReqId', Max35Text, False)

	@IssrDsclsrReqId.deleter
	def IssrDsclsrReqId(self):
		del self._IssrDsclsrReqId
		self._IssrDsclsrReqId = base_types.UninitialisedField(self, 'IssrDsclsrReqId', Max35Text, False)

	@property
	def ShrhldrsDsclsrRcrdDt(self):
		return self._ShrhldrsDsclsrRcrdDt

	@ShrhldrsDsclsrRcrdDt.setter
	def ShrhldrsDsclsrRcrdDt(self, value):
		self._ShrhldrsDsclsrRcrdDt = value if value is not None else base_types.UninitialisedField(self, 'ShrhldrsDsclsrRcrdDt', DateFormat46Choice, False)

	@ShrhldrsDsclsrRcrdDt.deleter
	def ShrhldrsDsclsrRcrdDt(self):
		del self._ShrhldrsDsclsrRcrdDt
		self._ShrhldrsDsclsrRcrdDt = base_types.UninitialisedField(self, 'ShrhldrsDsclsrRcrdDt', DateFormat46Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrDsclsrReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldrsDsclsrRcrdDt', type=DateFormat46Choice, min=1, max=1, mutex_group=None, array=False),
	))