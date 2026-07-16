# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalEnquiryRequestType1Code
from . import ExternalPaymentControlRequestType1Code
from . import GenericIdentification1

class RequestType4Choice(base_types._BaseFieldType):

	__slots__ = ["_Enqry", "_PmtCtrl", "_Prtry"]
	@property
	def Enqry(self):
		return self._Enqry

	@Enqry.setter
	def Enqry(self, value):
		self._Enqry = value if value is not None else base_types.UninitialisedField(self, 'Enqry', ExternalEnquiryRequestType1Code, False)

	@Enqry.deleter
	def Enqry(self):
		del self._Enqry
		self._Enqry = base_types.UninitialisedField(self, 'Enqry', ExternalEnquiryRequestType1Code, False)

	@property
	def PmtCtrl(self):
		return self._PmtCtrl

	@PmtCtrl.setter
	def PmtCtrl(self, value):
		self._PmtCtrl = value if value is not None else base_types.UninitialisedField(self, 'PmtCtrl', ExternalPaymentControlRequestType1Code, False)

	@PmtCtrl.deleter
	def PmtCtrl(self):
		del self._PmtCtrl
		self._PmtCtrl = base_types.UninitialisedField(self, 'PmtCtrl', ExternalPaymentControlRequestType1Code, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification1, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Enqry', type=ExternalEnquiryRequestType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCtrl', type=ExternalPaymentControlRequestType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))