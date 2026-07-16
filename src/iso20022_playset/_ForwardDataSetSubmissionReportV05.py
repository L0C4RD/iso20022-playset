# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import CertificateDataSet2
from . import CommercialDataSet5
from . import DataSetSubmissionReferences4
from . import InsuranceDataSet1
from . import MessageIdentification1
from . import OtherCertificateDataSet2
from . import PendingActivity2
from . import SimpleIdentificationInformation
from . import TransportDataSet5

class ForwardDataSetSubmissionReportV05(base_types._BaseFieldType):

	__slots__ = ["_BuyrBk", "_CertDataSet", "_CmonSubmissnRef", "_ComrclDataSet", "_InsrncDataSet", "_OthrCertDataSet", "_ReqForActn", "_RltdTxRefs", "_RptId", "_SellrBk", "_Submitr", "_TrnsprtDataSet"]
	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if value is not None else base_types.UninitialisedField(self, 'BuyrBk', BICIdentification1, False)

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = base_types.UninitialisedField(self, 'BuyrBk', BICIdentification1, False)

	@property
	def CertDataSet(self):
		return self._CertDataSet

	@CertDataSet.setter
	def CertDataSet(self, value):
		self._CertDataSet = value if value is not None else base_types.UninitialisedField(self, 'CertDataSet', CertificateDataSet2, True)

	@CertDataSet.deleter
	def CertDataSet(self):
		del self._CertDataSet
		self._CertDataSet = base_types.UninitialisedField(self, 'CertDataSet', CertificateDataSet2, True)

	@property
	def CmonSubmissnRef(self):
		return self._CmonSubmissnRef

	@CmonSubmissnRef.setter
	def CmonSubmissnRef(self, value):
		self._CmonSubmissnRef = value if value is not None else base_types.UninitialisedField(self, 'CmonSubmissnRef', SimpleIdentificationInformation, False)

	@CmonSubmissnRef.deleter
	def CmonSubmissnRef(self):
		del self._CmonSubmissnRef
		self._CmonSubmissnRef = base_types.UninitialisedField(self, 'CmonSubmissnRef', SimpleIdentificationInformation, False)

	@property
	def ComrclDataSet(self):
		return self._ComrclDataSet

	@ComrclDataSet.setter
	def ComrclDataSet(self, value):
		self._ComrclDataSet = value if value is not None else base_types.UninitialisedField(self, 'ComrclDataSet', CommercialDataSet5, False)

	@ComrclDataSet.deleter
	def ComrclDataSet(self):
		del self._ComrclDataSet
		self._ComrclDataSet = base_types.UninitialisedField(self, 'ComrclDataSet', CommercialDataSet5, False)

	@property
	def InsrncDataSet(self):
		return self._InsrncDataSet

	@InsrncDataSet.setter
	def InsrncDataSet(self, value):
		self._InsrncDataSet = value if value is not None else base_types.UninitialisedField(self, 'InsrncDataSet', InsuranceDataSet1, False)

	@InsrncDataSet.deleter
	def InsrncDataSet(self):
		del self._InsrncDataSet
		self._InsrncDataSet = base_types.UninitialisedField(self, 'InsrncDataSet', InsuranceDataSet1, False)

	@property
	def OthrCertDataSet(self):
		return self._OthrCertDataSet

	@OthrCertDataSet.setter
	def OthrCertDataSet(self, value):
		self._OthrCertDataSet = value if value is not None else base_types.UninitialisedField(self, 'OthrCertDataSet', OtherCertificateDataSet2, True)

	@OthrCertDataSet.deleter
	def OthrCertDataSet(self):
		del self._OthrCertDataSet
		self._OthrCertDataSet = base_types.UninitialisedField(self, 'OthrCertDataSet', OtherCertificateDataSet2, True)

	@property
	def ReqForActn(self):
		return self._ReqForActn

	@ReqForActn.setter
	def ReqForActn(self, value):
		self._ReqForActn = value if value is not None else base_types.UninitialisedField(self, 'ReqForActn', PendingActivity2, False)

	@ReqForActn.deleter
	def ReqForActn(self):
		del self._ReqForActn
		self._ReqForActn = base_types.UninitialisedField(self, 'ReqForActn', PendingActivity2, False)

	@property
	def RltdTxRefs(self):
		return self._RltdTxRefs

	@RltdTxRefs.setter
	def RltdTxRefs(self, value):
		self._RltdTxRefs = value if value is not None else base_types.UninitialisedField(self, 'RltdTxRefs', DataSetSubmissionReferences4, True)

	@RltdTxRefs.deleter
	def RltdTxRefs(self):
		del self._RltdTxRefs
		self._RltdTxRefs = base_types.UninitialisedField(self, 'RltdTxRefs', DataSetSubmissionReferences4, True)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', MessageIdentification1, False)

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if value is not None else base_types.UninitialisedField(self, 'SellrBk', BICIdentification1, False)

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = base_types.UninitialisedField(self, 'SellrBk', BICIdentification1, False)

	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if value is not None else base_types.UninitialisedField(self, 'Submitr', BICIdentification1, False)

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = base_types.UninitialisedField(self, 'Submitr', BICIdentification1, False)

	@property
	def TrnsprtDataSet(self):
		return self._TrnsprtDataSet

	@TrnsprtDataSet.setter
	def TrnsprtDataSet(self, value):
		self._TrnsprtDataSet = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtDataSet', TransportDataSet5, False)

	@TrnsprtDataSet.deleter
	def TrnsprtDataSet(self):
		del self._TrnsprtDataSet
		self._TrnsprtDataSet = base_types.UninitialisedField(self, 'TrnsprtDataSet', TransportDataSet5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertDataSet', type=CertificateDataSet2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmonSubmissnRef', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclDataSet', type=CommercialDataSet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncDataSet', type=InsuranceDataSet1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCertDataSet', type=OtherCertificateDataSet2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTxRefs', type=DataSetSubmissionReferences4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtDataSet', type=TransportDataSet5, min=0, max=1, mutex_group=None, array=False),
	))