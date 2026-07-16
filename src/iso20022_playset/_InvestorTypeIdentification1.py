# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestorClassificationType1Code
from . import Max1025Text

class InvestorTypeIdentification1(base_types._BaseFieldType):

	__slots__ = ["_InvstrTpId", "_InvstrTpIdNrrtv"]
	@property
	def InvstrTpId(self):
		return self._InvstrTpId

	@InvstrTpId.setter
	def InvstrTpId(self, value):
		self._InvstrTpId = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpId', InvestorClassificationType1Code, False)

	@InvstrTpId.deleter
	def InvstrTpId(self):
		del self._InvstrTpId
		self._InvstrTpId = base_types.UninitialisedField(self, 'InvstrTpId', InvestorClassificationType1Code, False)

	@property
	def InvstrTpIdNrrtv(self):
		return self._InvstrTpIdNrrtv

	@InvstrTpIdNrrtv.setter
	def InvstrTpIdNrrtv(self, value):
		self._InvstrTpIdNrrtv = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpIdNrrtv', Max1025Text, False)

	@InvstrTpIdNrrtv.deleter
	def InvstrTpIdNrrtv(self):
		del self._InvstrTpIdNrrtv
		self._InvstrTpIdNrrtv = base_types.UninitialisedField(self, 'InvstrTpIdNrrtv', Max1025Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrTpId', type=InvestorClassificationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpIdNrrtv', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
	))