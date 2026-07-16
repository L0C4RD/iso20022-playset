# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptanceResult6
from . import OriginalMandate11Choice
from . import OriginalMessageInformation1
from . import SupplementaryData1

class MandateAcceptance8(base_types._BaseFieldType):

	__slots__ = ["_AccptncRslt", "_OrgnlMndt", "_OrgnlMsgInf", "_SplmtryData"]
	@property
	def AccptncRslt(self):
		return self._AccptncRslt

	@AccptncRslt.setter
	def AccptncRslt(self, value):
		self._AccptncRslt = value if value is not None else base_types.UninitialisedField(self, 'AccptncRslt', AcceptanceResult6, False)

	@AccptncRslt.deleter
	def AccptncRslt(self):
		del self._AccptncRslt
		self._AccptncRslt = base_types.UninitialisedField(self, 'AccptncRslt', AcceptanceResult6, False)

	@property
	def OrgnlMndt(self):
		return self._OrgnlMndt

	@OrgnlMndt.setter
	def OrgnlMndt(self, value):
		self._OrgnlMndt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMndt', OriginalMandate11Choice, False)

	@OrgnlMndt.deleter
	def OrgnlMndt(self):
		del self._OrgnlMndt
		self._OrgnlMndt = base_types.UninitialisedField(self, 'OrgnlMndt', OriginalMandate11Choice, False)

	@property
	def OrgnlMsgInf(self):
		return self._OrgnlMsgInf

	@OrgnlMsgInf.setter
	def OrgnlMsgInf(self, value):
		self._OrgnlMsgInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgInf', OriginalMessageInformation1, False)

	@OrgnlMsgInf.deleter
	def OrgnlMsgInf(self):
		del self._OrgnlMsgInf
		self._OrgnlMsgInf = base_types.UninitialisedField(self, 'OrgnlMsgInf', OriginalMessageInformation1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncRslt', type=AcceptanceResult6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMndt', type=OriginalMandate11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgInf', type=OriginalMessageInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))