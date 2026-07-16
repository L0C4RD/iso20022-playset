# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExchangePolicy2Code
from . import Max35Text
from . import Max70Text
from . import PartyType5Code

class TriggerInformation2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_SrcId", "_TrggrSrc", "_TrggrTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max70Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max70Text, False)

	@property
	def SrcId(self):
		return self._SrcId

	@SrcId.setter
	def SrcId(self, value):
		self._SrcId = value if value is not None else base_types.UninitialisedField(self, 'SrcId', Max35Text, False)

	@SrcId.deleter
	def SrcId(self):
		del self._SrcId
		self._SrcId = base_types.UninitialisedField(self, 'SrcId', Max35Text, False)

	@property
	def TrggrSrc(self):
		return self._TrggrSrc

	@TrggrSrc.setter
	def TrggrSrc(self, value):
		self._TrggrSrc = value if value is not None else base_types.UninitialisedField(self, 'TrggrSrc', PartyType5Code, False)

	@TrggrSrc.deleter
	def TrggrSrc(self):
		del self._TrggrSrc
		self._TrggrSrc = base_types.UninitialisedField(self, 'TrggrSrc', PartyType5Code, False)

	@property
	def TrggrTp(self):
		return self._TrggrTp

	@TrggrTp.setter
	def TrggrTp(self, value):
		self._TrggrTp = value if value is not None else base_types.UninitialisedField(self, 'TrggrTp', ExchangePolicy2Code, False)

	@TrggrTp.deleter
	def TrggrTp(self):
		del self._TrggrTp
		self._TrggrTp = base_types.UninitialisedField(self, 'TrggrTp', ExchangePolicy2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrggrSrc', type=PartyType5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrggrTp', type=ExchangePolicy2Code, min=1, max=1, mutex_group=None, array=False),
	))