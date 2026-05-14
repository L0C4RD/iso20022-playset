# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvestorClassificationType1Code import InvestorClassificationType1Code
from ._Max1025Text import Max1025Text

class InvestorTypeIdentification1(base_types._BaseFieldType):

	__slots__ = ["_InvstrTpId", "_InvstrTpIdNrrtv"]
	@property
	def InvstrTpId(self):
		return self._InvstrTpId

	@InvstrTpId.setter
	def InvstrTpId(self, value):
		self._InvstrTpId = value if type(value) != base_types.auto else self.make_default("InvstrTpId")

	@InvstrTpId.deleter
	def InvstrTpId(self):
		del self._InvstrTpId
		self._InvstrTpId = None

	@property
	def InvstrTpIdNrrtv(self):
		return self._InvstrTpIdNrrtv

	@InvstrTpIdNrrtv.setter
	def InvstrTpIdNrrtv(self, value):
		self._InvstrTpIdNrrtv = value if type(value) != base_types.auto else self.make_default("InvstrTpIdNrrtv")

	@InvstrTpIdNrrtv.deleter
	def InvstrTpIdNrrtv(self):
		del self._InvstrTpIdNrrtv
		self._InvstrTpIdNrrtv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrTpId', type=InvestorClassificationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpIdNrrtv', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
	))